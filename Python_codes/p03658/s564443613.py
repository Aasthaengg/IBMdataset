import sys
N,K = map(int,input().split())
int_array = list(map(int,input().split()))

if N < 0 or K < 0 or N > 50 or K > 50:
    sys.exit()
for I in int_array:
    if I > 50:
        sys.exit()

rev_sort_int_array = sorted(int_array,reverse=True)
result = 0
for J in range(K):
    result += rev_sort_int_array[J]

print(result)