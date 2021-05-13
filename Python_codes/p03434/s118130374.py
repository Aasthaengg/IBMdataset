n=int(input())
s=list(map(int,input().split()))
s.sort(reverse=True)

alice=sum(s[::2])
bob=sum(s)-alice
print(alice-bob)