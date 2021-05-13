antennas = [int(input()) for _ in range(5)]
distance = int(input())
antennas_distance = abs(sorted(antennas)[len(antennas)-1] - sorted(antennas)[0])
print(':(' if antennas_distance > distance else 'Yay!')