N = int(raw_input())
num_list = map(int, raw_input().split())

print " ".join(map(str,num_list))
for i in range(1, N):
    v = num_list[i]
    j = i - 1
    while j >= 0 and num_list[j] > v:
       num_list[j+1] = num_list[j]
       j-=1
    num_list[j+1] = v
    print " ".join(map(str,num_list))