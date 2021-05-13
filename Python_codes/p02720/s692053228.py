def make(i):
    if int(i) > 3234566667:  return
    lun.append(int(i))
    if int(i[-1]) - 1 >= 0:  make(i + str(int(i[-1]) - 1))
    make(i + i[-1])
    if int(i[-1]) + 1 <= 9:  make(i + str(int(i[-1]) + 1))

lun = []
for i in range(1, 10):  make(str(i))
lun = sorted(lun)
print(lun[int(input()) - 1])