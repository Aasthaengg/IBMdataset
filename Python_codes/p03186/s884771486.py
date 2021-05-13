untasty , tasty_ant , poison = input().split()
untasty = int(untasty)
tasty_ant = int(tasty_ant)
poison = int(poison)
tasty = 0

if (untasty + tasty_ant) == poison:
    tasty = tasty_ant + poison
elif (untasty + tasty_ant) > poison:
    tasty = tasty_ant + poison
elif (untasty + tasty_ant) < poison:
    tasty = untasty + (2 * tasty_ant) + 1

print(tasty)
