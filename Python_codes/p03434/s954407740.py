n,s = int(raw_input()),map(int,raw_input().split())
s.sort(key = lambda x:-x)
print sum(s[0:n:2]) - sum(s[1:n:2])