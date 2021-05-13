N = int(input())
A = 0#末尾がA
B = 0#先頭がB
BA = 0#先頭がB かつ 末尾がA
AB = 0#ABの数

for i in range(N):
    s = input()
    AB += s.count("AB")
    if s[0] == "B":
        B += 1
    if s[-1] == "A":
        A += 1
    if s[0] == "B" and s[-1] == "A":
        BA += 1
        B -= 1
        A -= 1
ans = 0
ans += AB

if min(A,B) > 0:
    ans += BA + 1
    A -= 1
    B -= 1
    ans += min(A,B)
else:
    ans += max(BA + min(1, max(A,B)) -1,0)
print(ans)
    
#if BA > max(A,B) - min(A,B):
#    ans += (BA - (max(A,B) - min(A,B))) / 2
#print(A,B,BA,AB)