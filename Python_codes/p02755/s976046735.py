A,B=map(int, input().split())

ans=1100
for i in range(1,1002):
    if int(i*0.08) ==A and int(i*0.1) ==B:
        if i < ans:
            ans =i

print(ans if ans <1100 else -1)