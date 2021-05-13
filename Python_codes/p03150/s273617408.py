import sys

input = sys.stdin.readline

S = input()
S = S.replace('\n','')
s_list = list(S)

K = "keyence"
k_list = list(K)

for start in range(len(s_list)):
    small_s_list = s_list[start:]
    if "".join(small_s_list)== K:
        print("YES")
        exit(0)

for end in reversed(range(len(s_list))):
    small_s_list = s_list[:end+1]
    if "".join(small_s_list)== K:
        print("YES")
        exit(0)
point = int(len(s_list)/2)
for delete_start in range(len(s_list)-point):
    if delete_start >= point:
        break
    for delete_end in reversed(range(len(s_list))):
        if delete_end < point:
            break
        small_s_list = s_list[:delete_start+1] + s_list[delete_end:]
        if "".join(small_s_list)== K:
            print("YES")
            exit(0)
print("NO")