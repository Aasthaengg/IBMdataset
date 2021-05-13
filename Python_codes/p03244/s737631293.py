from collections import Counter
n = int(input())
arr = list(map(int, input().split()))

odd_list =[]
num_list =[]

for i in range(n):
    if i%2 == 0:
        odd_list.append(arr[i])
    if i%2 != 0:
        num_list.append(arr[i])

odd_count = Counter(odd_list)
num_count = Counter(num_list)
odd1 = odd_count[odd_count.most_common()[0][0]]
num1 = num_count[num_count.most_common()[0][0]]

if odd1 != num1:
    print(n-odd_count.most_common()[0][1]-num_count.most_common()[0][1])
    exit()

if len(set(arr)) == 1:
    print(int(n/2))
    exit()

if len(set(num_list))==1 and len(set(odd_list))==1:
    print(0)
    exit()

if len(set(odd_count)) == 1 and len(set(num_count)) != 1:
    num2 = num_count[num_count.most_common()[1][0]]
    if odd_list[0] == num_count.most_common()[0][0]:
        print(int(n/2)-num2)
        exit()
    if odd_list[0] != num_count.most_common()[0][0]:
        print(int(n/2)-num1)
        exit()

if len(set(odd_count)) != 1 and len(set(num_count)) == 1:
    odd2 = odd_list[odd_count.most_common()[1][0]]
    if num_list[0] == odd_count.most_common()[0][0]:
        print(int(n/2)-odd2)
        exit()
    if num_list[0] != odd_count.most_common()[0][0]:
        print(int(n/2)-odd1)
        exit()

odd2 = odd_count[odd_count.most_common()[1][0]]
num2 = num_count[num_count.most_common()[1][0]]

if odd_count.most_common()[0][0] != num_count.most_common()[0][0]:
    print(n-odd1-num1)

if odd_count.most_common()[0][0] == num_count.most_common()[0][0]:
    print(min(n-odd1-num2, n-odd2-num1))