

num_of_votes = int(input())

poll = {}

for i in range(num_of_votes):
    entry = input()
    
    if (poll.get(entry) == None):
        poll[entry] = 0
    
    poll[entry] += 1

max_votes = 0
most_voted_entries = []

for key in poll:
    num_of_votes = poll[key]

    if num_of_votes > max_votes:
        most_voted_entries = [ key ]
        max_votes = num_of_votes
    elif num_of_votes == max_votes:
        most_voted_entries.append(key)

for entry in sorted(most_voted_entries):
    print(entry)