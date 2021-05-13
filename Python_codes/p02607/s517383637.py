n = int(input())
a = input().split()

answer =0
for i,v in enumerate(a):
    if i%2==0 and int(v)%2==1:
        answer+=1
print(answer)