N = int(input())

keta = 1
keta_max_list = []
keta_max_list.append(0)

keta_max_list.append(26**(keta))
while True:
    if N <= keta_max_list[keta]:
        break
    keta += 1
    keta_max_list.append(keta_max_list[keta-1] + 26**(keta))
#print(keta,keta_max_list)

keta_list = [0 for _ in range(keta+1)]

for i in range(keta, 0, -1):  # keta ～　1 桁目までループ
    for j in range(1,27):
        if (N-keta_max_list[i-1])/26**(i-1) <= j:
            keta_list[i] = j
            N -= j*26**(i-1)
            break
            
ans_list = []
for i in range(keta, 0, -1):
    ans_list.append(chr(97+keta_list[i]-1))
ans = "".join(ans_list)

print(ans)