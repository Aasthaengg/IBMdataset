import math

N, A, B = map(int, input().split())
v = list(map(int, input().split()))

v.sort()
max_avg = sum(v[-A:]) / A

min_selected = v[- A]
selected = 0
for i in range(len(v) - A, len(v)):
    if v[i] == min_selected:
        selected += 1
    else:
        break
        
not_selected = 0
for i in range(0, len(v) - A):
    if v[i] == min_selected:
        not_selected +=  1
        
case_num = 0
if selected != A:        
    case_num = math.factorial(selected + not_selected) // (math.factorial(selected) * math.factorial(not_selected))
else:
    for i in range(A, min(B, selected + not_selected) + 1):
        case_num += math.factorial(selected + not_selected) // (math.factorial(i) * math.factorial(selected + not_selected - i))
print(max_avg)
print(case_num)