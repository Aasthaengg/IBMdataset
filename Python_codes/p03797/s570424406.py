S,C = list(map(int,input().split()))

if 2*S > C:
    ans = C//2
else:
    ans = S+(C-2*S)//4
    
print(ans)