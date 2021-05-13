# Shuffle

end = 0
shuffled = []

while end == 0:
    phrase = input()
    if phrase == '-':
        end += 1
    else:
        shuffleTimes = int(input())
        for i in range(shuffleTimes):
            shufflePosition = int(input())
            phrase = phrase[shufflePosition:] + phrase[:shufflePosition]
        shuffled.append(phrase)

for array in shuffled:
    print(array)

