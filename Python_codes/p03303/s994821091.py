s = input()
mod = int(input())
for i in range(len(s)):
    if i%mod==0: print(s[i],end="")
print()