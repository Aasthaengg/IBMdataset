w=raw_input().lower()
sum=0
while 1:
    s=raw_input()
    if s=="END_OF_TEXT": break
    a=map(str, s.lower().split())
    sum+=a.count(w)
print sum