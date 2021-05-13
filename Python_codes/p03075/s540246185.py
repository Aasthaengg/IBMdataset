ais = [int(raw_input()) for _ in range(5)]
k = int(raw_input())
print ':(' if ais[0] + k < ais[-1] else 'Yay!' 