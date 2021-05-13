n = int(raw_input())
i=1
x=i
nums = []


def include3():
    global n
    global i
    global x
    global nums

    while True:
        if x % 10 == 3:
            nums.append(str(i))
            if end_check_num():
                return 0
            return 1

        x /= 10
        if x==0:
            if end_check_num():
                return 0
            return 1
    return 1

def end_check_num():
    global n
    global i
    global x

    i+=1
    if i <= n:
        return False
    return True


while True:
    x=i
    if x % 3==0:
        nums.append(str(i))
        if end_check_num():
            break
        continue
    if 0==include3():
        break

print " " + " ".join(nums)