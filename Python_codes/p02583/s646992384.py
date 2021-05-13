N = int(input())
L_list = list(map(int, input().split()))

count = 0
i = 0
while i < N:
    a = L_list[i]
    j = 0
    while j < i:
        b = L_list[j]
        k = 0
        while k < j:
            c = L_list[k]
            k += 1
            if a == b or b == c or c == a:
                continue
            if a + b > c and b + c > a and c + a > b:
                count += 1
        j += 1
    i += 1
                
print(count)

