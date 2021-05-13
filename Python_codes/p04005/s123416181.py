a,b,c = map(int, input().split())

ans1=a*b*abs(c//2 - (c-c//2))
ans2=b*c*abs(a//2 - (a-a//2))
ans3=a*c*abs(b//2 - (b-b//2))

print(min(ans1,ans2,ans3))