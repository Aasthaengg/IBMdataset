from collections import defaultdict
n = int(input())
v = [int(x) for x in input().split()]

even_ocr = defaultdict(int) # v[0], v[2], ..., で各数が何回現れるか
odd_ocr = defaultdict(int)  # v[1], v[3], ..., で各数が何回現れるか

for i in range(n // 2):
    even_ocr[v[2 * i]] += 1
    odd_ocr[v[2 * i + 1]] += 1

even_max_num = 0;  even_max_ocr = 0;
odd_max_num = 0;  odd_max_ocr = 0;
for (num, ocr) in even_ocr.items():
    if ocr > even_max_ocr:
        even_max_ocr = ocr
        even_max_num = num

for (num, ocr) in odd_ocr.items():
    if ocr > odd_max_ocr:
        odd_max_ocr = ocr
        odd_max_num = num

if even_max_num != odd_max_num:
    ans = n - even_max_ocr - odd_max_ocr
else:
# 偶数番目に一番多く現れる数と奇数番目に一番多く現れる数が同じ
    even_next_num = 0;  even_next_ocr = 0;
    odd_next_num = 0;  odd_next_ocr = 0;
    for (num, ocr) in even_ocr.items():
        if num != even_max_num and ocr > even_next_ocr:
            even_next_ocr = ocr
            even_next_num = num

    for (num, ocr) in odd_ocr.items():
        if num != odd_max_num and ocr > odd_next_ocr:
            odd_next_ocr = ocr
            odd_next_num = num

    if even_next_ocr + odd_max_ocr > even_max_ocr + odd_next_ocr:
        # 偶数番目は二番目に多い数、奇数番目は一番多い数に揃える
        ans = n - even_next_ocr - odd_max_ocr
    else:
        ans = n - even_max_ocr - odd_next_ocr

print(ans)