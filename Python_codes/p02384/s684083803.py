class dice():
    
    def __init__(self, nums):
        self.pos = []
        self.pos.extend(nums)
    
    def right(self, et, ef):
        # t : 上面のラベル
        # f : 正面のラベル

        t = self.pos.index(et)  # 上面（の扱いになっている）のラベルを取得
        f = self.pos.index(ef)  # 前面（の扱いになっている）のラベルを取得
        
        # u,f,r
        dr = [(1,2,4,3),(0,3,5,2),(0,1,5,4),(0,4,5,1),(0,2,5,3),(1,3,4,2)]
        r = (dr[t].index(f) + 1) % 4
        print(self.pos[dr[t][r]])

d = dice([int(x) for x in input().split()])
q = int(input())
for i in range(q):
    d.right(*map(int, input().split()))
