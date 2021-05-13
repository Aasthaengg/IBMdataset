import copy
H, W, K = map(int, input().split())
lst = []
num = 0
for i in range(H):
    arrange = input()
    num += arrange.count('#')
    lst.append(arrange)
# print(num)
count = 0

for i in range(2**H):
    # print("初期化")
    rlst = copy.copy(lst)
    counted = 0
    rstr = str(format(i, '0' + str(H) + 'b'))
    # print("rstr:" + rstr)
    while '1' in rstr:
        index = rstr.find('1')
        counted += rlst[index].count('#')
        rlst[index] = "." * W
        rstr = rstr.replace('1','0',1)
    # print(counted)
    for j in range(2**W):
        ccounted = counted
        clst = copy.copy(rlst)
        cstr = str(format(j, '0' + str(W) + 'b'))
        # print("cstr:" + cstr)
        while '1' in cstr:
            index = cstr.find('1')
            dlst = ""
            for k in range(H):
                dlst += clst[k][index]
                clst[k] = clst[k][:index] + '.' + clst[k][index+1:]
            ccounted += dlst.count("#")
            cstr = cstr.replace('1','0',1)
        # print(clst)
        # print(str(num-ccounted))
        if num - ccounted == K:
            count += 1

print(count)