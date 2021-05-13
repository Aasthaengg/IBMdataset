N = int(input())
"""
リスト最下位までの人数は確実にいる，
あとはリスト最下位の点数が0になるまで
1刻みに人がいた場合が最大人数
"""
List = sorted([tuple(map(int, input().split(" "))) for i in range(N)],reverse=True)
print(List[0][0]+List[0][1])
