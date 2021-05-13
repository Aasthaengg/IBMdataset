k = int(input())
ans = [i for i in range(50)]
# print(ans)
def inv_process(arr,i):
    arr[i] += 50
    for j in range(50):
        if j == i:
            continue
        else:
            arr[j]-=1
loop = k//50
sup = k-loop*50

for i in range(50):
    ans[i] += loop


for i in range(sup):
    inv_process(ans,i)

print(50)
for i in range(49):
    print(ans[i],end=" ")
print(ans[-1])