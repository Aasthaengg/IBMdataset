K = int(input())
N = 50

print(N)
br = (K-1)//50
pos = K-50*br
ans_list = list(range(br,br+50))
for i in range(pos,N):
    ans_list[i] -= 1*pos
for i in range(0,pos):
    ans_list[i] = ans_list[i]+N-(1*pos)+1

print(" ".join(map(str,ans_list)))