A,B = map(int,input().split())

ans_array = [ [1] * 100 if i < 50 else [0] * 100 for i in range(100)]

# print(ans_array)
A -= 1
B -= 1
i = 1
j = 1
# print(ans_array[i])
while A != 0:
    ans_array[i][j] = 0
    A -= 1
    j += 2
    if j >= 100:
        i += 2
        j = 1

i = 51
j = 1
while B != 0:
    ans_array[i][j] = 1
    B -= 1
    j += 2
    if j >= 100:
        i += 2
        j = 1

print(100,100)
for ans in ans_array:
    ans_str = "".join(map(str,ans)).replace("0",".").replace("1","#")
    print(ans_str)