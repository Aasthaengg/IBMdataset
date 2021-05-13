import sys

def set_list_flag(es):
    return len(list(set(es))) == 1

input = sys.stdin.readline

S = input()
S = S.replace('\n','')
s_list = list(S)

s_result = s_list
next_s_result = []
min_count = 10**6

if set_list_flag(s_list):
    print(0)
    exit(0)
for s in s_list:
    count = 0
    while not set_list_flag(next_s_result):
        count += 1
        next_s_result = []
        for i in range(len(s_result)):
            cur_s = s_result[i]
            nex_s = s_result[i+1]
            get_s = nex_s
            
            if cur_s == s:
                get_s = s

            next_s_result.append(get_s)
            if i+1 == len(s_result)-1:
                break
        s_result = next_s_result

    min_count = min(min_count,count)
    s_result = s_list
    next_s_result = []


print(min_count)