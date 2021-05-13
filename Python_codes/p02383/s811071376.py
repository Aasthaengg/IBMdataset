
class Dice:

	top = 0
	south = 1
	east = 2
	west = 3
	north = 4
	bottom = 5

	def __init__(self, faces):
		self.faces = faces

	def roll(self, direction):

		top_ = self.top
		south_ = self.south
		east_ = self.east
		west_ = self.west
		north_ = self.north
		bottom_ = self.bottom

		if direction == 'E':
			self.top = west_
			self.east = top_
			self.bottom = east_
			self.west = bottom_
		elif direction == 'N':
			self.top = south_
			self.south = bottom_
			self.bottom = north_
			self.north = top_
		elif direction == 'S':
			self.top = north_
			self.south = top_
			self.bottom = south_
			self.north = bottom_
		elif direction == 'W':
			self.top = east_
			self.east = bottom_
			self.bottom = west_
			self.west = top_
		else:
			return

	def get_top(self):
		return faces[self.top]

faces = list(map(int, input().split()))
directions = str(input())

dice = Dice(faces)

for direction in directions:
	dice.roll(direction)

print(dice.get_top())
