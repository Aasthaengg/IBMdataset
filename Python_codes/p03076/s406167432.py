def resolve():
    '''
    code here
    '''
    import math

    dishes = [int(input()) for _ in range(5)]
    dev_dis = [item % 10 for item in dishes if item % 10 != 0]
    dev_dis.sort()

    res = sum(dishes)
    if dev_dis:
        for item in dev_dis[1:]:
            if item != 0:
                res += 10 -item

    print(res)

if __name__ == "__main__":
    resolve()
