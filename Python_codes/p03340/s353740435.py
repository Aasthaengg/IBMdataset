N = int(input())
A_array = list(map(int,input().split()))

start = 0
end = 0
ans = 0
a_sum = A_array[0]
a_xor = A_array[0]

for start in range(N):
    while end != (N-1):
        # print(start,end,a_sum,a_xor)
        a_sum_new = a_sum + A_array[end+1]
        a_xor_new = a_xor ^ A_array[end+1]
        if a_sum_new == a_xor_new:
            end += 1
            a_sum = a_sum_new
            a_xor = a_xor_new
        else:
            break
    # print("!",a_sum,a_xor,start,end)
    ans += (end-start+1)
    a_sum -= A_array[start]
    a_xor = a_xor ^ A_array[start]

print(ans)

