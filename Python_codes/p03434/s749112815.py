n=int (input())
card=list(map(int, input().strip().split()))
card.sort(reverse=True)
a=0
b=0
for i in range(n):
    if i%2==0:
        a=a+card[i]
    elif i%2==1:
        b=b+card[i]
print(a-b)