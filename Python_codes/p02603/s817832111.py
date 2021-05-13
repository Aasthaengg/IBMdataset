n=int(input())
a=list(map(int,input().split()))

a=[300]+a+[0] #先頭と末尾にダミーデータ
money=1000
numStock=0
LAST_UP=1
LAST_DN=2
last_change=LAST_DN

def buy(value):
    global money,numStock
    numStock+=money//value
    money-=numStock*value

def sell(value):
    global money,numStock
    money+=value*numStock
    numStock=0

for i in range(1,n+1):
    if a[i-1]<a[i]:
        last_change=LAST_UP
        if a[i]>a[i+1]: sell(a[i])
    elif a[i-1]>a[i]:
        last_change=LAST_DN
        if a[i]<a[i+1]: buy(a[i])
    else: # if a[i-1]==a[i]
        if a[i]<a[i+1]: #買い または 待ち
            if last_change==LAST_DN: buy(a[i])
        elif a[i]>a[i+1]: #売り または 待ち
            if last_change==LAST_UP: sell(a[i])

sell(a[n]) #最後に株の残があれば売る

print(money)