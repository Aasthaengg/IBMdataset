s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)

S=''.join(s)
T=''.join(t)

ans_ = [S,T]
ans_.sort()

ans='Yes'
if ans_[0] == T:
    ans='No'
    
print(ans)