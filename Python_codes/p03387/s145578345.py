N_List = sorted(list(map(int,input().split())))
cnt = 0
if N_List[0] + 2 <= N_List[2]:
    cnt += (N_List[2] - N_List[0])//2
    N_List[0] += ((N_List[2] - N_List[0])//2) * 2

if N_List[1] + 2 <= N_List[2]:
    cnt += (N_List[2] - N_List[1])//2
    N_List[1] += ((N_List[2] - N_List[1])//2) * 2

if N_List.count(max(N_List)) == 2:
    cnt += 2
elif N_List.count(max(N_List)) == 1:
    cnt += 1
else:
    cnt += 0
print(cnt)