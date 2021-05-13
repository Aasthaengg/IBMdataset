nums =[int(e) for e in input().split()]
yakusuu = []
yakusuu_count = 0
for j in range(1,nums[2]+1):
    if nums[2]%j== 0:
        yakusuu.append(j)
for k in range(len(yakusuu)):
    if nums[0]<=yakusuu[k] and yakusuu[k]<=nums[1]:
        yakusuu_count += 1
print(yakusuu_count)
