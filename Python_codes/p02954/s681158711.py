S = input()
l = [0]*len(S)

left,right,bol = 0,0,0
for i in range(len(S)):
    if bol == 0:
        if S[i] == "R":
            left += 1
        else:
            bol = 1
            right += 1
            j = i
    else:
        if S[i] == "L":
            right += 1
        else:
            l[j-1] = -(-left//2) + right//2
            l[j] = left//2 + -(-right//2)
            left,right,bol = 1,0,0

l[j-1] = -(-left//2) + right//2
l[j] = left//2 + -(-right//2)
print(*l)