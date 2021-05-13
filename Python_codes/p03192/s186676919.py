import io

str_in = list(input())
count = 0

for i in range(4):
    if str_in[i] == '2':
        count+=1

print(count)