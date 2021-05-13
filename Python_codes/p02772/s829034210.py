a = int(input())
b = list(map(int, input().split()[:a]))
my_list = []
score = 0
for i in b:
    if i%2==0:
        my_list.append(i)
for i in my_list:
    if i%3==0 or i%5==0:
        score += 1
if len(my_list) == score:
    print("APPROVED")
else:
    print("DENIED")