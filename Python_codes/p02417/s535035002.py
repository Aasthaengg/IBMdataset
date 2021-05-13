import sys

count = [0 for _ in range(26)]

for line in sys.stdin:
    array = line
    char = ["" for _ in range(len(array))]
    for i in range(len(array)):
        char[i] = array[i:i+1]
    for c in char:
        for i in range(26):
            if c == chr(i+ord("A")) or c == chr(i+ord("a")):
                count[i] += 1


for i in range(26):
    print("{0} : {1}".format(chr(i+ord("a")), count[i]))