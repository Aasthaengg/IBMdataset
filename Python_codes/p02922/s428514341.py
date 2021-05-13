#ABC139B
a,b = map(int,input().split())
ans = 0 
outlet = 1
while b>outlet:
    outlet = outlet - 1
    outlet = outlet + a
    ans = ans + 1
print(ans)