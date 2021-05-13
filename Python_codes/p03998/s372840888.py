a = list(input())
b = list(input())
c = list(input())

num_li = [a,b,c]

now = 0
while True:
    if len(num_li[now])==0:
        print('A' if now==0 else 'B' if now==1 else 'C');exit()

    x = num_li[now].pop(0)
    now = 0 if x=='a' else 1 if x=='b' else 2