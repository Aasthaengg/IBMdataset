N = int(input())

digit = 0
max = 0
while True:
    if N <= max:
        break
    digit += 1
    max += 26 ** digit
under_digit = 0

for i in range(1, digit):
    under_digit += 26 ** i

order = N - under_digit - 1 #0_index
# print("order:", order)

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

remain = order
now = digit - 1

# print("digit:", digit)
ans = ""
# print(ans)
# counter = 0
if remain == 0:
    ans = "a" * digit
while remain != 0:
    # print("---------------")
    # counter += 1
    # print("counter", counter)
    # if counter >= 10:
    #     break

    ans = ans + letter[remain // (26 ** now)]
    remain %= 26 ** now
    now -= 1
    # print("ans:", ans, "remain:", remain, "now:", now)
    if remain == 0 and now == 0:
        ans = ans + "a"
        break

print(ans)
