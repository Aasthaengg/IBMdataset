N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

H_gap = list(map(lambda x: abs(T - x * 0.006 - A), H))
place_num = H_gap.index(min(H_gap)) + 1
print(place_num)
