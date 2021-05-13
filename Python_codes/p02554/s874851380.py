n=int(input())
a=1000000007
ans=(10**n%a-9**n%a-9**n%a+8**n%a)%a
print(ans)