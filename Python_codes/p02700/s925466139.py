HPT,ATT,HPA,ATA=map(int,input().split())
for i in range(1000):
  HPA += -ATT
  if HPA <= 0:
    print("Yes")
    break
  HPT += -ATA
  if HPT <= 0:
    print("No")
    break