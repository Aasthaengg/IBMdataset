from collections import namedtuple

def main():
    n,m = map(int,input().split())
    Req = namedtuple("Req","a b")
    requests = []
    for _ in range(m): #m個の要望
        a,b = map(int,input().split())
        requests.append(Req(a,b))

    requests.sort(key=lambda x:x.b)
    pre_cut = -1 #前回切断した端の左側の位置
    counter = 0 #切断の回数
    for i,req in enumerate(requests):
        if not req.a <= pre_cut < req.b:
            counter += 1
            pre_cut = req.b - 1
        else:
            continue
    print(counter)







if __name__ == '__main__':
    main()
