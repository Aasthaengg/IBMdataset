import collections as cl

# 全街のつながりは保証されていて、橋は3本固定なので、枝分かれしてなければたどり着けるはず
def main() :
    bridges = []
    for i in range(3) :
        in_list = [int(i) for i in input().split()]
        bridges.extend(in_list)
    
    c = cl.Counter(bridges)
    com = c.most_common()
    if (com[0][1] == 2 and com[1][1] == 2 and com[2][1] == 1 and com[3][1] == 1) :
        print("YES")
    else :
        print("NO")
        
        
    






main()