N = int(input())

count_ab = 0
count_start_b = 0
count_finish_a = 0
count_start_b_finish_a = 0
for i in range(N):
    s = input()
    count_ab += s.count('AB')
    # print(s, s[0], s[-1])
    if s[0] == 'B' and s[-1] == 'A':
        count_start_b_finish_a += 1
    elif s[0] == 'B':
        count_start_b += 1
    elif s[-1] == 'A':
        count_finish_a += 1

# print(count_start_b_finish_a, count_finish_a, count_start_b)

if not count_start_b_finish_a:
    print(count_ab + min(count_finish_a, count_start_b))
elif max(count_finish_a, count_start_b) > 0 and count_start_b_finish_a:
    print(count_ab + count_start_b_finish_a + min(count_finish_a, count_start_b))
elif count_start_b_finish_a:
    print(count_ab + count_start_b_finish_a - 1)