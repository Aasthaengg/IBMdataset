s=input()
k=int(input())
print(sorted(list({s[i:i+f] for i in range(len(s)) for f in range(1,k+1)}))[k-1])