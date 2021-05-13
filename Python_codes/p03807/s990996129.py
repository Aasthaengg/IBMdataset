N=input()
o = len([i for i in input().split() if int(i)%2!=0])
print("YES" if o%2==0 else "NO")