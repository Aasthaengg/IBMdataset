#import torch
class solution(object):

    def __init__(self, D: int, T: int, S: int)-> None:
        self.D = D
        self.T = T
        self.S = S
    
    def solve(self)->bool:
        return ['No','Yes'][(self.D/self.S) <= self.T]
    
if __name__=='__main__':
    # x = int(input())
    D,T,S= map( int , input().split())
    problem = solution(D, T, S)
    ans = problem.solve()
    print(ans)
